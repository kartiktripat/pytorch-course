Oct 15th 
1. Learned how to make a tensor.
2. Used reshape, zeros and arange functions
3. * is used to multiply 2 tensors of same shape element wise.
4. @ is used for matrix multiplication contigent on having the inner sizes matching.
5. tensor[row, column] is used to a row and column.
6. : is used for all of them.
7. default for decimal type is float32 and whole numbers is int64


Oct 16th
1. y.backward() calculates how much y changes with x at its current value and stores the result in x.grad. For y = x² + 2x at x = 3, x.grad is 8. Afterward, PyTorch clears the temporary values needed for that calculation, not x.grad. Calling backward again on the same y can fail because those temporary values are gone. Recomputing y gives it fresh values to work with.
2. When I calculate y again and call y.backward(), the new gradient gets added to the value already stored in x.grad. It does not replace the old value. To get only the new gradient, I need to clear x.grad before calling backward again.
3. Calling x.grad.zero_() clears the gradient stored in x.grad by setting it to zero. It does not change x itself. After rebuilding y and calling y.backward(), x.grad holds the new gradient without adding the old one. The underscore in zero_() means it changes the existing gradient tensor directly.
4. Integers can’t have gradients because a gradient answers what happens under a tiny change, and integer values can’t be nudged in tiny steps. Training updates also use fractional changes, which don’t fit integer tensors. That’s why PyTorch refuses requires_grad on int tensors; use floating point tensors when you need gradients.
5. requires_grad = True tells PyTorch to track this tensor for learning. It records how later results depend on it so backward can compute gradients and store them in the tensor’s grad field. If it’s False, PyTorch won’t track it and no gradient will be produced for that tensor.


Oct 17th
1. the training loop consists of five  steps: forward pass, loss calculation, zeroing gradients, backward pass, and updating weights. these directly map to the sequential execution in your code.
2. using in-place subtraction (-=) inside a no_grad() block ensures that weights are updated directly without tracking these operations in the computation graph, avoiding the errors that occur with standard assignment (w = w - ...).
3. gradients must be zeroed out before every round because PyTorch accumulates them by default, meaning they would stack up and cause incorrect updates if not reset.
4. setting a learning rate that is too large causes the updates to overshoot the minimum, leading to divergence where the loss actually increases rather than decreases.