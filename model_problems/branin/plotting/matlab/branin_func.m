%READ SURFPACK RESPONSE SURFACE
%load -ascii test_data.txt
load -ascii data/test_data.spd
 
x1 =test_data(:,1);
x2 =test_data(:,2);
fs =test_data(:,3);

x=unique(x1);  % turn x1 into a unique range of values
y=unique(x2);  % turn y1 into a unique range of values

z=zeros(length(y),length(x)); % preallocate space for the z surface

  for m=1:length(x)
   for n=1:length(y)
     z(n,m)=fs(find(x1==x(m) & x2==y(n)));
     % reorder the z1 column into a rectangular matrix
   end
  end
  
%PLOT SURFPACK RESPONSE SURFACE
%mesh(x,y,z)
%surf(x,y,z,'EdgeColor','none','FaceColor','interp','FaceLighting','phong')
%contourf(x,y,z,50)



%COMPUTE THE BRANIN FUNCTION
minX = -5; maxX = 10;
minY = 0; maxY = 15;

xa = linspace(minX,maxX,100);
ya = linspace(minY,maxY,100);

[xa1,xa2] = meshgrid(xa,ya);

fa = ( xa2 - 5 ./ ( 4 * pi^2 ) * xa1 .^ 2 + ( 5 / pi ) .* xa1 - 6 ) .^ 2 + 10 * ( 1 - 1 / ( 8 * pi ) ) .* cos( xa1 ) + 10;



%READ THE SAMPLING POINTS AND PLOT SURFPACK RESPONSE SURFACE WITH THE POINTS
load -ascii data/table_out.dat;
xx1=table_out(:,2);
xx2=table_out(:,3);
ff = ( xx2 - 5.1 ./ ( 4 * pi^2 ) * xx1 .^ 2 + ( 5 / pi ) .* xx1 - 6 ) .^ 2 + 10 * ( 1 - 1 / ( 8 * pi ) ) .* cos( xx1 ) + 10;




%TO PLOT BOTH SOLUTIONS
figure(1)
contourf(x,y,z,50)
hold on;
%plot3(xx1,xx2,ff,'ok','MarkerFaceColor','yellow','MarkerSize',6)
plot(xx1,xx2,'ok','MarkerFaceColor','yellow','MarkerSize',6)
title('Surrogate')

figure(2)
contourf(xa1,xa2,fa,50);
%hold on;
%plot3(xx1,xx2,ff,'ok','MarkerFaceColor','yellow','MarkerSize',6)
%plot(xa1,xa2,'ok','MarkerFaceColor','yellow','MarkerSize',6)
title('Analytical solution')





%ADDITIONAL PLOTS

%analytical
%surf(xa1,xa2,fa);
%surf(xa1,xa2,fa,'EdgeColor','none')
%surf(xa1,xa2,fa,'EdgeColor','none','FaceColor','interp')
%surf(xa1,xa2,fa,'EdgeColor','none','FaceColor','interp','FaceLighting','phong')
%contour(xa1,xa2,fa,50);
%contour3(xa1,xa2,fa,50);



%surrogate
%surf(x,y,z);
%surf(x,y,z,'EdgeColor','none')
%surf(x,y,z,'EdgeColor','none','FaceColor','interp')
%surf(x,y,z,'EdgeColor','none','FaceColor','interp','FaceLighting','phong')
%contour(x,y,z,50);
%contour3(x,y,z,50);



%contourf(x,y,z,50);
%hold on;
%plot(xx1,xx2,'ok','MarkerFaceColor','black','MarkerSize',6)



%surrogate
%surf(x,y,z,'EdgeColor','none','FaceColor','interp','FaceLighting','phong')
%hold on;
%plot3(xx1,xx2,ff,'ok','MarkerFaceColor','black','MarkerSize',6)



%analytical
%surf(xa1,xa2,fa,'EdgeColor','none','FaceColor','interp','FaceLighting','phong')
