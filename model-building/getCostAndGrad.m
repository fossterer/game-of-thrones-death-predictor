function [J, grad] = getCostAndGrad(theta, X, y)
  m = size(X, 1);
 
  J = 0;
  grad = zeros(size(theta));

  h_x = sigmoid(X*theta);
  J = (1/m)*sum(-y.*log(h_x) - (1-y).*log(1-h_x));

  grad = (1/m)*((h_x - y)'*(X));

end
