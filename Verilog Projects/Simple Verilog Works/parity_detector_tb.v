module parity_detector_tb();
reg clk=0,x;
wire z;
parity_detector DUT(.clk(clk),.x(x),.z(z));
always #5 clk=~clk;

initial  
begin  
$dumpfile("parity_detector.vcd");
$dumpvars(0,parity_detector_tb);
$monitor($time,"clk=%b,x=%b,z=%b",clk,x,z);

#2 x=0; #10x=1; #10x=1; #10x=0; #10x=1; #10x=1;
#10x=0; #10x=0; #10x=1;
#10 $finish;
end


endmodule