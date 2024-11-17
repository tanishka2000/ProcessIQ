import matplotlib.pyplot as plt
import matplotlib.patches as patches
import ezdxf
import re

def parse_prompt(prompt):
    """
    Parse the prompt to extract elements and connections for the P&ID based on
    the order of operations (using bold text as delimiters).
    """
    elements = []
    connections = []

    # Use regex to find operations (text between **)
    operations = re.findall(r"\\(.?)\\*", prompt)

    current_x = 10  # Starting x position
    padding = 35   # Increased padding between elements

    # Create elements based on operations
    for i, operation in enumerate(operations):
        element_width = 10 + len(operation) * 3
        position = (current_x, 10)
        elements.append({"type": "operation",
                         "name": operation,
                         "position": position,
                         "width": element_width})
        current_x += element_width + padding

    # Connect elements sequentially
    for i in range(len(elements) - 1):
        connections.append({"source": elements[i]["name"], "target": elements[i + 1]["name"]})

    return elements, connections


def generate_pid(prompt):
    """
    Generates a P&ID visualization using matplotlib and exports it to DXF.
    """
    elements, connections = parse_prompt(prompt)
    elements, connections = parse_prompt(prompt)
    if not elements:
        print("Error: No elements found in the prompt.")
        return None

    fig, ax = plt.subplots(figsize=(12, 4))  # Increased figure size

    # Calculate bounds for layout border
    min_x = min(element["position"][0] - element["width"] / 2 for element in elements)
    max_x = max(element["position"][0] + element["width"] / 2 for element in elements)
    min_y = min(element["position"][1] for element in elements)
    max_y = max(element["position"][1] for element in elements)

    # Add layout border with padding
    border_padding = 10
    # Calculate border height, providing a default if no tanks are found
    tank_radius = next((elem["width"] / 2 for elem in elements if elem["type"] == "tank"), 10)  # Default to 10 if no tank

    # OR you can have a conditional that checks for existence of tanks
    # tank_elements = [elem for elem in elements if elem["type"] == "tank"]
    # if tank_elements:
    #    tank_radius = tank_elements[0]["width"] / 2
    # else:
    #    tank_radius = 10 #Default value

    border_height = 2 * (tank_radius + border_padding)
    ax.add_patch(patches.Rectangle(
        (min_x - border_padding, min_y - border_height / 2),  # Adjusted for tank centering
        max_x - min_x + 2 * border_padding,
        border_height,
        facecolor="none",
        edgecolor="black"
    ))

    for element in elements:
        x, y = element["position"]
        width = element["width"]

        if element["type"] == "tank":
            # Center the tank horizontally

            ax.add_patch(patches.Circle((x, y), width / 2, facecolor="white", edgecolor="black"))
            ax.text(x, y, element["name"], ha="center", va="center", bbox=dict(facecolor="white", edgecolor="black", boxstyle="circle,pad=0.5"))
        else:
            ax.add_patch(patches.Rectangle((x - width / 2, y - 2.5), width, 5, facecolor="white", edgecolor="black"))
            ax.text(x, y, element["name"], ha="center", va="center", bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.5"))



    for connection in connections:
        source_elem = next(elem for elem in elements if elem["name"] == connection["source"])
        target_elem = next(elem for elem in elements if elem["name"] == connection["target"])
        source_x, source_y = source_elem["position"]
        target_x, target_y = target_elem["position"]
        source_width = source_elem["width"]
        target_width = target_elem["width"]

        source_x += source_width / 2
        target_x -= target_width / 2
        ax.plot([source_x, target_x], [source_y, target_y], color="black", linestyle="-", linewidth=1)

    # Center the content vertically
    ax.set_ylim(min_y - border_height , min_y + border_height / 2)
    ax.set_xlim(min_x - 20, max_x + 20)

    ax.axis('off')
    ax.set_aspect("equal")



    plt.show()

    # Export to DXF (example - you'll need to add entity creation logic)
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()
    # Add DXF entities to msp based on elements and connections
    doc.saveas("pid_diagram.dxf")

    return fig
