module nbit_counter_tb();

reg clk=0,clr;
wire [0:7]count;
nbit_counter DUT(.clk(clk),.clr(clr),.count(count));
always #5 clk=~clk;
initial 
begin
$dumpfile("nbit_counter.vcd");
$dumpvars(0,nbit_counter_tb);
$monitor($time,"clk=%b,clr=%b,count=%b",clk,clr,count);

clr=1;
#3 clr=0;

#200 $finish;
end


endmodule