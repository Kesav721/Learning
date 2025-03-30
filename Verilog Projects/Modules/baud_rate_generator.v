module baud_generator #(
    parameter BAUD_RATE = 9600,
    parameter CLK_FREQ = 50000000
)(
    input wire clk,
    input wire rst,
    output reg tick
);
    localparam BIT_PERIOD = CLK_FREQ / BAUD_RATE;
    reg [15:0] counter = 0;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            counter <= 0;
            tick <= 0;
        end else if (counter < BIT_PERIOD - 1) begin
            counter <= counter + 1;
            tick <= 0;
        end else begin
            counter <= 0;
            tick <= 1;
        end
    end
endmodule
