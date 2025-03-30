`timescale 1ns/1ps

module uart_tx_tb;
    reg clk, rst, tx_start;
    reg [7:0] data;
    wire tx, tx_busy;

    // Instantiate the UART TX module
    uart_tx uut (
        .clk(clk),
        .rst(rst),
        .tx_start(tx_start),
        .data(data),
        .tx(tx),
        .tx_busy(tx_busy)
    );

    always #10 clk = ~clk; // 50 MHz clock (20 ns period)

    initial begin
        clk = 0;
        rst = 1;
        tx_start = 0;
        data = 8'hA5; // Data to send: 10100101

        #50 rst = 0;  // Release reset
        #50 tx_start = 1;  
        #20 tx_start = 0;  

        #200000; // Wait for transmission
        $finish;
    end

endmodule
