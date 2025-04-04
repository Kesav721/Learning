module test_pattern_generator_tb();
reg clk,reset,mode;
wire [3:0]pattern;
test_pattern_gen DUT (.clk(clk),.reset(reset),.mode(mode),.pattern(pattern));
initial begin 
$dumpfile("test_pattern_generator.vcd");
$dumpvars(0,test_pattern_generator_tb);
$monitor($time,"clk=%b,reset=%b,mode=%b,pattern=%b",clk,reset,mode,pattern);
end 
initial begin 
clk =0;
 forever 
 #5 clk=~clk;
end 
initial begin 
// static mode
reset=1;mode=0;
#5 reset=0;
//dynamic mode
#10 reset=1;mode=1;
#5 reset=0;
 #100$finish;
end
endmodule