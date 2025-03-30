module uart_rx_shift (
    input wire clk,
    input wire rst,
    input wire tick,     
    input wire sample,    
    input wire rx,        
    output reg [7:0] data,
    output reg done       
);
    reg [7:0] shift_reg;
    reg [3:0] bit_index;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            shift_reg <= 0;
            bit_index <= 0;
            done <= 0;
        end else if (sample) begin
            shift_reg[bit_index] <= rx;
            bit_index <= bit_index + 1;

            if (bit_index == 7) done <= 1; // Reception complete
        end
    end

    assign data = shift_reg;
endmodule
