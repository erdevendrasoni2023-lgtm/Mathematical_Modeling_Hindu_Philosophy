# Mathematical Modeling of Hindu Philosophy

This repository contains the Python codes and LaTeX files developed for the research paper titled "Mathematical Modeling of Hindu Philosophy: Zero, One, and Infinity". This project explores the mathematical representation of fundamental concepts in Hindu philosophy, such as Nirguna (Zero), Saguna (One), and Anant (Infinity), through continuous, discrete, and limit-based models.

## Project Structure

- `python_codes/`: Contains all Python scripts used to generate the visualizations of the mathematical models.
  - `formula1_continuous_model.py`: Code for the continuous model ($f(t) = t / (1 + t)$).
  - `formula2_discrete_model.py`: Code for the discrete model ($A_n = 2^{n-1}$).
  - `formula3_limit_based_model.py`: Code for the conceptual visualization of the limit-based model.
  - `combined_model_visualization.py`: Code for the combined visualization of Formula 1 and Formula 2.
- `latex_paper/`: Contains LaTeX files, including the comparative table of the models.
  - `comparison_table.tex`: LaTeX source code for the detailed comparison table of the models.
- `images/`: Stores all generated graph images and conceptual diagrams.

## Mathematical Models

This research proposes three core mathematical models:

1.  **Continuous Model ($f(t) = \frac{t}{1+t}$):**
    * Represents the asymptotic progression from the formless void (Nirguna) to manifest unity (Saguna).
    * Visualized in `formula1_continuous_model.py`.
    
2.  **Discrete Model ($A_n = 2^{n-1}$):**
    * Illustrates the hierarchical, step-by-step creation from Saguna towards infinite consciousness (Anant).
    * Visualized in `formula2_discrete_model.py`.
    
3.  **Limit-Based Model ($\lim_{x\rightarrow\infty}(0+x^{n})$):**
    * Symbolically unifies Nirguna (0), Saguna (1), and Anant ($\infty$) as facets of a single divine reality.
    * Conceptual visualization in `formula3_limit_based_model.py`.
    
## Combined Visualization

An integrated graph showing the relationship between the continuous and discrete models.

## How to Use the Code

1.  **Prerequisites:** Ensure you have Python installed with `matplotlib` and `numpy` libraries.
2.  **Run the scripts:** Navigate to the `python_codes/` directory and run any script using `python your_script_name.py`.
3.  **LaTeX Table:** The `comparison_table.tex` file can be compiled using a LaTeX distribution (e.g., Overleaf) to generate a PDF.

## Contribution

Feel free to explore, use, and suggest improvements to the models or code.

---
**Author:** Devendra Soni
**Research Paper:** [https://zenodo.org/records/17089852](https://zenodo.org/records/17089852)
