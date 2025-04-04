module d_ff(d,clk,q,qbar);
input d,clk;
output reg q=0;
output qbar;
always  @(posedge clk)
case(d)
1'b0 : q<=1'b0;
1'b1 : q<=1'b1;
endcase
assign qbar =~q;
endmodule