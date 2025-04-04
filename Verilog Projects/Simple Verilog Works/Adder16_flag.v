module adder_16b(
    input [15:0] x,y,
    output [15:0] z,
    output sign,
    output zero,
    output carry,
    output parity,
    output overflow
    );
    assign{carry,z}=x+y;
    assign sign=z[15];
    assign zero=~|z;
    assign parity=~^z;
    assign overflow=(x[15]&y[15]&~z[15])|(~x[15]&~y[15]&z[15]);
endmodule