#!/usr/bin/env python3
"""Offline explorer for Creagent's symbolic TOE graph. Python stdlib only."""

from __future__ import annotations

import argparse
from collections import deque
import json
from pathlib import Path
import sys

GRAPH_PATH = Path(__file__).resolve().parents[1] / "assets" / "ontology.json"


def load_graph(path: Path = GRAPH_PATH) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(graph: dict) -> list[str]:
    errors: list[str] = []
    nodes = graph.get("nodes", [])
    layers = graph.get("layers", [])
    edges = graph.get("edges", [])
    ids = [node.get("id") for node in nodes]
    layer_ids = [layer.get("id") for layer in layers]
    if len(ids) != len(set(ids)):
        errors.append("duplicate node id")
    if len(layer_ids) != len(set(layer_ids)):
        errors.append("duplicate layer id")
    if not nodes:
        errors.append("no nodes")
    for required in ("viewer", "one", "abyss", "moon", "sun", "yggdrasil", "bardo", "ouroboros"):
        if required not in ids:
            errors.append(f"required node missing: {required}")
    for node in nodes:
        if not all(field in node for field in ("id", "label", "kind", "description", "epistemic")):
            errors.append(f"incomplete node: {node.get('id', '?')}")
        if "layer" in node and node["layer"] not in layer_ids:
            errors.append(f"unknown layer in node {node.get('id')}: {node['layer']}")
        if node.get("epistemic") not in ("source", "model-inference", "unresolved"):
            errors.append(f"unknown epistemic label in node {node.get('id')}")
    for index, edge in enumerate(edges):
        if edge.get("source") not in ids or edge.get("target") not in ids:
            errors.append(f"edge {index} references unknown node")
        if edge.get("epistemic") not in ("source", "model-inference", "unresolved"):
            errors.append(f"edge {index} missing recognized epistemic status")
        if not edge.get("type") or not edge.get("note"):
            errors.append(f"edge {index} missing type or note")
    if [layer["color"] for layer in layers] != ["red", "yellow", "green", "blue", "purple"]:
        errors.append("color bands out of declared order")
    return errors


def find_path(graph: dict, origin: str, destination: str) -> list[dict] | None:
    """Shortest path in *undirected* graph, preserving edge provenance."""
    known = {node["id"] for node in graph["nodes"]}
    if origin not in known or destination not in known:
        raise ValueError("unknown node; use 'list --kind node' to inspect choices")
    if origin == destination:
        return []
    adjacency = {node_id: [] for node_id in known}
    for edge in graph["edges"]:
        adjacency[edge["source"]].append((edge["target"], edge, "forward"))
        adjacency[edge["target"]].append((edge["source"], edge, "reverse"))
    queue = deque([origin])
    seen = {origin}
    parent = {}
    while queue:
        current = queue.popleft()
        for neighbor, edge, direction in adjacency[current]:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            parent[neighbor] = (current, edge, direction)
            if neighbor == destination:
                parts = []
                pointer = destination
                while pointer != origin:
                    prev, link, traverse = parent[pointer]
                    parts.append({"from": prev, "to": pointer, "relationship": link["type"],
                                  "epistemic": link["epistemic"], "direction": traverse,
                                  "note": link["note"]})
                    pointer = prev
                return list(reversed(parts))
            queue.append(neighbor)
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Explore Creagent's symbolic relational map")
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("validate", help="validate graph structure and source labels")
    listing = sub.add_parser("list", help="list nodes or layers")
    listing.add_argument("--kind", choices=("node", "layer"), default="node")
    show = sub.add_parser("show", help="show one node")
    show.add_argument("node")
    neighbors = sub.add_parser("neighbors", help="show direct relationships")
    neighbors.add_argument("node")
    path = sub.add_parser("path", help="shortest symbolic graph path (undirected)")
    path.add_argument("origin")
    path.add_argument("destination")
    args = parser.parse_args(argv)
    try:
        graph = load_graph()
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load ontology: {error}", file=sys.stderr)
        return 2
    errors = validate(graph)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if args.action == "validate":
        print(f"VALID: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges, {len(graph['layers'])} layers")
        return 0
    if args.action == "list":
        for item in graph["nodes" if args.kind == "node" else "layers"]:
            print(f"{item['id']}: {item['label']}")
        return 0
    nodes = {node["id"]: node for node in graph["nodes"]}
    if args.action in ("show", "neighbors") and args.node not in nodes:
        print(f"Unknown node: {args.node}", file=sys.stderr)
        return 2
    if args.action == "show":
        print(json.dumps(nodes[args.node], indent=2, ensure_ascii=False))
        return 0
    if args.action == "neighbors":
        matches = [edge for edge in graph["edges"] if args.node in (edge["source"], edge["target"])]
        for edge in matches:
            other = edge["target"] if edge["source"] == args.node else edge["source"]
            print(f"{args.node} ↔ {other}: {edge['type']} [{edge['epistemic']}]; {edge['note']}")
        return 0
    if args.action == "path":
        try:
            segments = find_path(graph, args.origin, args.destination)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        if segments is None:
            print("No connection found")
            return 1
        print(f"Symbolic graph route: {args.origin} → {args.destination} (undirected traversal)")
        if not segments:
            print("Same node; zero edges")
        for segment in segments:
            print(f"  {segment['from']} → {segment['to']} | {segment['relationship']} "
                  f"[{segment['epistemic']}, {segment['direction']}] | {segment['note']}")
        print("This is not a physical route, proof of an afterlife, or a causal claim.")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())