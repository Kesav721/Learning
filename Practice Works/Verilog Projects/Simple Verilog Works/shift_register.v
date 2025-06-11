module shift_register_4b(
    input clk, 
    input clr, 
    input A, 
    output reg B, 
    output reg C, 
    output reg D, 
    output reg E
);
always @(posedge clk or negedge clr)
begin 
    if (!clr) begin  // Active LOW Reset
        B <= 0;
        C <= 0;
        D <= 0;
        E <= 0;
    end
    else begin 
        E <= D;
        D <= C;
        C <= B;
        B <= A;  // New input shifts in
    end 
end
endmodule
