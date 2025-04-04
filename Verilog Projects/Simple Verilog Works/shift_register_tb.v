module shift_register_4b_tb();
reg clk=0,clr,A;
wire B,C,D;
wire E;
shift_register_4b DUT(clk,clr,A,B,C,D,E);
always 
#5 clk=~clk;
initial 
begin 
$dumpfile("shift_register_4b.vcd");
$dumpvars(0,shift_register_4b_tb);
$monitor($time,"clk=%b,clr=%b,A=%b,B=%b,C=%b,D=%b,E=%b",clk,clr,A,B,C,D,E);
#2 clr=0;#5clr=1;
end
initial begin #2;
repeat(2)

#10 A=0;
#10 A=0;
#10 A=1;
#10 A=1;

#200 $finish;
end

endmodule