x = 0:pi/100:2*pi;
y = sin(x);

figure;
subplot(2,1,1);
plot(x,y);
xlabel('$x_1$','interpreter','latex');
xlabel('$y_1$','interpreter','latex');

subplot(2,1,2);
plot(x,y);
xlabel('$x_2$','interpreter','latex');
xlabel('$y_2$','interpreter','latex');
matlab2tikz('test.tikz', 'height', '\figureheight', 'width', '\figurewidth');