module bitwise_rotator_tb();
reg clk,reset,rotate_dir;
reg[7:0]data_in;
wire[7:0]data_out;
bitwise_rotator DUT(.clk(clk),.reset(reset),.rotate_dir(rotate_dir),.data_in(data_in),.data_out(data_out));
initial begin 
clk=0;
forever #5 clk=~clk;
end 
initial begin 
reset=1;
data_in = 8'b10110011;

rotate_dir =0;

#10 reset=0;
#10 rotate_dir=0;
#10 rotate_dir=1;

#20 $finish; 
end 
initial begin 
$dumpfile("bitwise_rotator.vcd");
$dumpvars(0,bitwise_rotator_tb);
$monitor($time,"clk=%b,reset=%b,rotate_dir=%b,data_in=%b,data_out=%b",clk,reset,rotate_dir,data_in,data_out);
end
endmodule