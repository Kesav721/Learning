module nor_gate(out,a,b);
output out;
input a,b;
wire c;
// set up power and ground lines
supply1 pwr;
supply0 gnd;
// pmos switches
pmos (c,pwr,b);
pmos (out,c,a);
// nmos switches
nmos (out,gnd,a);
nmos (out,gnd,b);
endmodule