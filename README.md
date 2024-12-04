# ProcessIQ

**ProcessIQ** is an AI-powered Piping and Instrumentation Diagram (P&ID) creation and analysis tool developed as part of the **Koru Problem Hunt Case Competition**. This repository contains:

1. **[Landing Page](https://processiq.onrender.com/) Code**: A showcase of the tool's potential with a user-friendly interface.
2. **Pilot Prototype Demo Code**: Demonstrates the core functionality of ProcessIQ by using the **Gemini API** to process user input and generate basic process flow diagrams.

---

## What are P&IDs?

**Piping and Instrumentation Diagrams (P&IDs)** are critical schematics that depict the interconnection of process equipment and instrumentation in industrial facilities. They play an essential role in multiple industries, including:

- **Chemical Processing**
- **Oil & Gas**
- **Pharmaceuticals**
- **Power Generation**

### Why are P&IDs Important?

- **Design**: Ensure precise planning of process systems.
- **Operation**: Aid in understanding and controlling industrial processes.
- **Maintenance**: Help identify equipment and instrumentation for troubleshooting.
- **Safety & Compliance**: Ensure adherence to industry regulations and standards.

---

## What We Aim to Achieve with ProcessIQ

ProcessIQ is designed to streamline and modernize P&ID workflows with the following **core capabilities**:

1. **P&ID Creation from Textual Input**:
   - Engineers can input textual descriptions of processes, and ProcessIQ will generate accurate P&ID schematics.
   
2. **Analysis of Existing P&IDs**:
   - Detect errors, inconsistencies, and optimization opportunities in current diagrams.
   
3. **Legacy Diagram Conversion**:
   - Simplify the digitization of legacy P&IDs into modern, editable formats.

4. **User-Friendly Interface**:
   - Tailored for both technical users (engineers) and non-technical users, ensuring accessibility and ease of use.

---

## Features of This Repository

### 1. **Landing Page Code**
   - A visually appealing and user-friendly interface showcasing ProcessIQ's functionality.
   - Built with HTML, CSS, and JavaScript, the landing page serves as the starting point for users to learn about the product.

### 2. **Pilot Prototype Demo Code**
   - Integrates the **Gemini API** to demonstrate the core functionality of ProcessIQ.
   - Users can input prompts describing a process, and the system generates a basic process flow diagram.
   - Built with Python and Flask, this prototype illustrates the potential of using AI for P&ID generation.

---

## Installation and Usage

### Prerequisites

- **Python 3.8+**
- Required Python packages (listed in `requirements.txt`)

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tanishka2000/ProcessIQ.git
   cd ProcessIQ
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Landing Page**:
   Open the `index.html` file in the `/` directory using any browser.

4. **Run the Pilot Prototype**:
   Navigate to the `/demo` directory and execute the following:
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

5. **Provide User Input**:
   - Use the interface to input a textual prompt (e.g., "Generate a P&ID for a water treatment facility").
   - The application processes the input via the **Gemini API** and generates a basic process flow diagram.

---

## Sample Input and Output

### Sample Input
**Prompt**:  
Generate a P&ID for a water treatment facility.

### Sample Output (Image Placeholder)
Attach an image of the generated process flow diagram here:
<img width="668" alt="Screenshot 2024-12-04 at 2 19 11 PM" src="https://github.com/user-attachments/assets/563ad735-4184-40a6-85e7-75145cfe4272">

---

## Future Development Goals

- **Advanced Diagram Analysis**:
  - Implement AI to analyze and suggest improvements for P&ID designs.
  
- **Integration of Computer Vision**:
  - Allow upload and analysis of scanned legacy diagrams.

- **Enhanced User Interface**:
  - Develop a more robust and intuitive interface for broader user adoption.

- **Export Options**:
  - Add support for exporting P&IDs in various file formats, such as PDF, CAD, or XML.

---

## Contributing

We welcome contributions to enhance ProcessIQ. To contribute:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes with clear messages.
4. Push to your branch and open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For questions or suggestions, please open an issue in this repository or reach out to the repository maintainers.
