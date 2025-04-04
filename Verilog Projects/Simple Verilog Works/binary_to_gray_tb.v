module code_converter_tb();
reg [3:0] A;
wire [3:0]B;

code_converter DUT (.A(A),.B(B));
initial begin   
A=$random();
#10 A=$random();
#10 A=$random();
#10 A=$random();
#10 A=$random();
#10 A=$random();
#10 A=$random();

#20 $finish;
end
initial begin 
$dumpfile("code_converter,vcd");
$dumpvars(0,code_converter_tb);
$monitor($time,"A=%b,B=%b",A,B);
end


endmodule