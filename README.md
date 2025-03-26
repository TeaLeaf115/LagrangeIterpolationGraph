# Lagrange Polynomial Interpolation Graph
I made this program to learn how to graph Lagrange interpolation equations using code. This is part of my learning how QR Codes work, but I went down a rabbit hole to see how these functions behaved because it is so cool!

### Equations used for formula
$$P_{n}(x)=\sum_{i=1}^{n}(y_k\times L_{n,k}(x))$$
$$L_{n,k}(x)=\prod_{i=0, \ \ i\neq k}^{n}(\frac{x-x_i}{x_k-x_i})$$
Combined Equation: $$P_{n}(x)=\sum_{i=1}^{n}(y_k\times \prod_{i=0, \ \ i\neq k}^{n}(\frac{x-x_i}{x_k-x_i}))$$

## Example Program Output:
![Lagrange Equation](https://github.com/TeaLeaf115/TeaLeaf115/blob/ab225b39f6da376bb59b2803289d1c33fec0c59d/assets/Figure_1.png)
