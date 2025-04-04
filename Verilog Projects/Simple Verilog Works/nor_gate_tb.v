
module nor_gate_tb();
reg a,b;
wire out;
nor_gate DUT(.a(a),.b(b),.out(out));
initial begin 
$dumpfile("nor_gate.vcd");
$dumpvars(0,nor_gate_tb);
$monitor($time,"a=%b,b=%b,out=%b",a,b,out);

a=1'b0;b=1'b0;
#5 a=1'b0;b=1'b1;
#5 a=1'b1;b=1'b0;
#5 a=1'b1;b=1'b1;
#100$finish;
end

endmodule