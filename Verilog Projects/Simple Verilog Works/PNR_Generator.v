module pnr_generator(clk,reset,pnr_out);
parameter WIDTH =8;
parameter SEED = 8'b11001010;
input clk,reset;
output  [WIDTH-1 : 0]pnr_out;
reg[WIDTH-1 : 0] state;

always @(posedge clk)begin 
if (reset) begin 
state <= SEED;
end 
else begin 
state <= (state + 7) ^ (state >> 3);
end 
end 
assign pnr_out = state;
endmodule