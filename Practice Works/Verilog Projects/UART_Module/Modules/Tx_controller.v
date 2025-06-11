module uart_tx_controller (
    input wire clk,
    input wire rst,
    input wire start,
    output reg load,
    output reg shift
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            load <= 0;
            shift <= 0;
        end else if (start) begin
            load <= 1;
        end else begin
            load <= 0;
            shift <= 1;
        end
    end
endmodule
