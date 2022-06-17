$fn=100;

difference() {

  translate([0,0,0])
        linear_extrude(height=1)
          import("logo_2d.svg", center=true);
}
translate([-1.68,0,0])
    cube([0.3,6,1]);