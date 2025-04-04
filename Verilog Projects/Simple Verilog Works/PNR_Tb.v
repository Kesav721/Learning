module pnr_generator_tb();
reg clk,reset;
wire [7:0] pnr_out;
pnr_generator DUT(.clk(clk),.reset(reset),.pnr_out(pnr_out));

initial begin 
clk=0; 
forever #5 clk=~clk;
end 
initial begin 
$dumpfile("pnr_generator.vcd");
$dumpvars(0,pnr_generator_tb);
$monitor($time,"clk=%b,reset=%b,pnr_out=%b",clk,reset,pnr_out);
end
initial begin 
reset =1;
#10;
reset =0;
#100;
$finish;
end

endmodule