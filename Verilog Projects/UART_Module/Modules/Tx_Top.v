module uart_tx (
    input wire clk,
    input wire rst,
    input wire tx_start,
    input wire [7:0] data,
    output wire tx,
    output wire tx_busy
);
    wire tick, load, shift;

    baud_generator #(.BAUD_RATE(9600), .CLK_FREQ(50000000)) baudgen (
        .clk(clk), .rst(rst), .tick(tick)
    );

    uart_tx_controller controller (
        .clk(clk), .rst(rst), .start(tx_start), .load(load), .shift(shift)
    );

    uart_tx_shift shift_reg (
        .clk(clk), .rst(rst), .tick(tick), .load(load), .shift(shift), 
        .data(data), .tx(tx), .busy(tx_busy)
    );

endmodule
