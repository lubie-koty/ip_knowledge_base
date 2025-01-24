import ipaddress
import json

import intervaltree


def load_knowledge_base_file(filename: str) -> list[dict[str, str]]:
    """
    Loads a JSON file stored in the data folder at the root of the project.
    """
    file_path = f"data/{filename}"
    with open(file_path, "r") as f:
        json_data = json.load(f)
    return json_data


def create_knowledge_base(data: list[dict]) -> intervaltree.IntervalTree:
    """
    Creates a knowledge base (`IntervalTree`) from a list of dictionaries
    containing pairs of ip_networks and their corresponding tags.
    """
    tags_by_ip_networks = {}
    for entry in data:
        network_tags = tags_by_ip_networks.setdefault(
            ipaddress.ip_network(entry["ip_network"]), set()
        )
        new_tag = entry["tag"]
        network_tags.add(new_tag)

    return intervaltree.IntervalTree(
        intervaltree.Interval(
            begin=int(ip_network.network_address),
            end=int(
                ip_network.broadcast_address
                if ip_network.num_addresses > 1
                else ip_network.network_address
            )
            + 1,
            data=tags,
        )
        for ip_network, tags in tags_by_ip_networks.items()
    )
