# Bezier

Create bezier curves, sample them at arbitrary points, and easily plot them.

Call with either a list of ordered pairs: `Bezier([(x0,y0), (x1,y1), ... , (xn,yn)])`

or a seperate list of x and y coordinates: `Bezier([x0, x1, ... , xn], [y0, y1, ... , yn])`

## Optional Parameters:

### points=False

If points is `False`, `Bezier` returns `(x, y)`, where x and y are lists of x and y coordinates, respectively.

If points is `True`, `Bezier` returns `[(x0, y0), (x1, y1), ... , (xn, yn)]`.

### step=1e-3

When slicing Bezier, if a step size is not provided this is used instead.

## Using Bezier

After creating the curve, retrieve points using the `__getitem__` function, similar to indexing a list.

```python
import bezier

bez = bezier.Bezier([1,3,4],[2,4,3])

x,y = bez[.2]
```

You can also slice `Bezier` to return several values at once. `start` and `stop` default to 0 and 1 respectively (or 1 and 0 if `step` is negative) and `step` will default to the value set at instanciation.

```python
x,y = bez[.1:.6:.001]
x,y = bez[::.01]
```

An empty slice object will return the entire curve (at the reolution set by `step`), which provies a quick way to plot the entire curve.

```python
import matplotlib.pyplot as plt
x,y = bez[:]
plt.plot(x, y)
```

Or, more succinctly:

```python
plt.plot(*bez[:])
```
