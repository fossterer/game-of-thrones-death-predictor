% Load training data
data = csvread('../data-preprocessing/output/training-data.txt');

% Separate into X and y
X = data(:, 2:3);
y = data(:, 4);

m = size(X, 1);
n = size(X, 2);

% Visualization of data:  Plot X1 and X2 on perpendicular axes where y=0 and y = 1 are differentiated
deadRows = X(y==1, :);
aliveRows = X(y==0, :);

figure; hold on;
plot(deadRows(:, 1), deadRows(:, 2), 'rx');
plot(aliveRows(:, 1), aliveRows(:, 2), 'go');
xlabel('No. of episode appearances');
ylabel('No. of victims killed');
legend('Dead', 'Alive');
hold off;
print -djpg outputs/scatterplot

% Set initalTheta to 0
initialTheta = zeros(n, 1);

% Design Cost Function


% Apply fminunc() to obtain best possible theta
options = optimset('GradObj', 'on', 'MaxIter', 400);
[theta, J, exit_flag] = ...
	fminunc(@(t)(getCostAndGrad(t, X, y)), initialTheta, options);
  
% Run against training data with new theta
predictions = predict(theta, X);
accuracy = mean(double(predictions==y))*100;

fprintf("For the calculated theta value [%f %f]', cost is %f and our accuracy is %f\n", theta(:), J, accuracy);
% Pick just one of those rows to demonstrate 'testing phase'