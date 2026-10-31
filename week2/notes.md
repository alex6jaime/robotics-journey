## Week 2 — Python tools for robotics

### What I learned
- Classes group data and behaviour. My `EncoderMotor` inherits from `Motor` and adds encoder-count conversion.
- Pytest uses assertions to check expected results automatically.
- NumPy arrays represent numerical data. `*` multiplies element by element; `@` performs matrix multiplication.
- A NumPy vector with shape `(3,)` has no explicit row or column orientation; `(3, 1)` is a column vector.
- `np.linalg.solve(A, b)` finds the unknown vector in `A @ x = b`.
- Rotation matrices transform points around the origin.
- Matplotlib plots numerical results, and equal axis scaling preserves geometric proportions.

### Problem I investigated
Pytest stopped while loading ROS testing code because `yaml` was missing. Using `--disable-plugin-autoload` allowed my standalone motor test to run. This bypassed the plugin dependency issue for that run.

### Reflection
The concept I understand best now is using NumPy and Matplotlib, as I have used them before and feel comfortable working with them to analyse data and create visualisations.

The concept I still need to practise is using classes and debugging. I need more practice so that I can develop a natural and automatic understanding of when classes are needed and how to use them effectively. I also want to become more confident with debugging so I can identify and fix errors independently.