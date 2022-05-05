$fn=100;

//translate([0,0,0.5]) {
//    cylinder(h=1, r=10, center=true);
//    translate([0,0,1])
//        linear_extrude(height=1)
//            import("logo_2d.svg", center=true);
//}

difference() {
//  cylinder(h=1, r=10)

  translate([0,0,0])
        linear_extrude(height=1)
          import("logo_2d.svg", center=true);
}
translate([-1.68,0,0])
    cube([0.3,6,1]);