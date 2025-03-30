module uart_tx_shift (
    input wire clk,
    input wire rst,
    input wire tick,      // Baud tick
    input wire load,      // Load new data
    input wire shift,     // Shift data out
    input wire [7:0] data,// 8-bit parallel data
    output reg tx,        // UART TX output
    output reg busy       // Transmission status
);
    reg [9:0] shift_reg; // Start bit, 8 data bits, Stop bit
    reg [3:0] bit_index;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            shift_reg <= 10'b1111111111;
            bit_index <= 0;
            tx <= 1;
            busy <= 0;
        end else if (load && !busy) begin
            shift_reg <= {1'b1, data, 1'b0}; // Load start, data, stop bit
            busy <= 1;
            bit_index <= 0;
        end else if (tick && busy) begin
            tx <= shift_reg[0];
            shift_reg <= shift_reg >> 1;
            bit_index <= bit_index + 1;

            if (bit_index == 9) busy <= 0; // Transmission complete
        end
    end
endmodule
