module debouncer(clk,btn_in,btn_out);
input clk,btn_in;
output reg btn_out;
reg q1,q2;
always @(posedge clk) begin 
q1 <= btn_in;
q2 <= q1;
btn_out <= q2;
end
endmodule