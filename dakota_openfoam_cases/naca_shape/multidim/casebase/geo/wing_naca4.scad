//	module airfoil() default to NACA-8412
//	camber_max - percent figure. ( range 0-9 )
//	camber_position - tenths   ( range 0-9 )
//	thickness - percentage relative to chord   ( range 0-99 )

//The module has default values of camber_max = 8, camber_position = 4, thickness = 12 
//these can be changed after when whe use the module
module airfoil(camber_max = 8, camber_position = 4, thickness = 12) 
{

	m = camber_max/100;
	p = camber_position/10;
	t = thickness/100;
	
//	pts = 25; // datapoints on each of upper and lower surfaces
	pts = 50; // datapoints on each of upper and lower surfaces
	
	function xx(i) = 1 - cos((i-1)*90/(pts-1));
	function yt(i) = t/0.2*(0.2969*pow(xx(i),0.5) - 0.126*xx(i)-0.3516*pow(xx(i),2) + 0.2843*pow(xx(i),3) - 0.1015*pow(xx(i),4));
	function yc(i) = xx(i)<p ? m/pow(p,2)*(2*p*xx(i) - pow(xx(i),2)) : m/pow(1-p,2)*(1 - 2*p + 2*p*xx(i) - pow(xx(i),2));
	function xu(j) = xx(j) - yt(j)*(sin(atan((yc(j)-yc(j-1))/(xx(j)-xx(j-1)))));
	function yu(j) = yc(j) + yt(j)*(cos(atan((yc(j)-yc(j-1))/(xx(j)-xx(j-1)))));
	function xl(j) = xx(j) + yt(j)*(sin(atan((yc(j)-yc(j-1))/(xx(j)-xx(j-1)))));
	function yl(j) = yc(j) - yt(j)*(cos(atan((yc(j)-yc(j-1))/(xx(j)-xx(j-1)))));

	polygon( points=[ 
 	// upper side front-to-back
	// here you need to define the same amount of panels as in pts
	[0,0],[xu(2),yu(2)],[xu(3),yu(3)],[xu(4),yu(4)],[xu(5),yu(5)],[xu(6),yu(6)],[xu(7),yu(7)],[xu(8),yu(8)],[xu(9),yu(9)],[xu(10),yu(10)],[xu(11),yu(11)],[xu(12),yu(12)],[xu(13),yu(13)],[xu(14),yu(14)],[xu(15),yu(15)],[xu(16),yu(16)],[xu(17),yu(17)],[xu(18),yu(18)],[xu(19),yu(19)],[xu(20),yu(20)],[xu(21),yu(21)],[xu(22),yu(22)],[xu(23),yu(23)],[xu(24),yu(24)],[xu(25),yu(25)],[xu(26),yu(26)],[xu(27),yu(27)],[xu(28),yu(28)],[xu(29),yu(29)],[xu(30),yu(30)],[xu(31),yu(31)],[xu(32),yu(32)],[xu(33),yu(33)],[xu(34),yu(34)],[xu(35),yu(35)],[xu(36),yu(36)],[xu(37),yu(37)],[xu(38),yu(38)],[xu(39),yu(39)],[xu(40),yu(40)],[xu(41),yu(41)],[xu(42),yu(42)],[xu(43),yu(43)],[xu(44),yu(44)],[xu(45),yu(45)],[xu(46),yu(46)],[xu(47),yu(47)],[xu(48),yu(48)],[xu(49),yu(49)],[xu(50),yu(50)],

	// lower side back to front
	// here you need to define the same amount of panels as in pts
	[xl(50),yl(50)],[xl(49),yl(49)],[xl(48),yl(48)],[xl(47),yl(47)],[xl(46),yl(46)],[xl(45),yl(45)],[xl(44),yl(44)],[xl(43),yl(43)],[xl(42),yl(42)],[xl(41),yl(41)],[xl(40),yl(40)],[xl(39),yl(39)],[xl(38),yl(38)],[xl(37),yl(37)],[xl(36),yl(36)],[xl(35),yl(35)],[xl(34),yl(34)],[xl(33),yl(33)],[xl(32),yl(32)],[xl(31),yl(31)],[xl(30),yl(30)],[xl(29),yl(29)],[xl(28),yl(28)],[xl(27),yl(27)],[xl(26),yl(26)],[xl(25),yl(25)],[xl(24),yl(24)],[xl(23),yl(23)],[xl(22),yl(22)],[xl(21),yl(21)],[xl(20),yl(20)],[xl(19),yl(19)],[xl(18),yl(18)],[xl(17),yl(17)],[xl(16),yl(16)],[xl(15),yl(15)],[xl(14),yl(14)],[xl(13),yl(13)],[xl(12),yl(12)],[xl(11),yl(11)],[xl(10),yl(10)],[xl(9),yl(9)],[xl(8),yl(8)],[xl(7),yl(7)],[xl(6),yl(6)],[xl(5),yl(5)],[xl(4),yl(4)],[xl(3),yl(3)],[xl(2),yl(2)],[0,0]
	] ); 
}


//airfoil(); 
//airfoil(8,4,12);

//We made a linear extrusion of airfoil to crete the 3d body, at this point we can change the default values
$fn=100;

curvature=2;
curvature_position=6;
airfoil_thickness=12;

linear_extrude(height = 1, center = true,convexity = 10)
{
airfoil(curvature,curvature_position,airfoil_thickness);
} 
