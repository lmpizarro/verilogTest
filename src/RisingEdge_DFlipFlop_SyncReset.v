// FPGA projects using Verilog/ VHDL 
// fpga4student.com
// Verilog code for D Flip FLop
// Verilog code for Rising edge D flip flop with Synchronous Reset input 
module RisingEdge_DFlipFlop_SyncReset(D,clk,sync_reset,Q);
 input D; // Data input 
 input clk; // clock input 
 input sync_reset; // synchronous reset 
 output reg Q; // output Q 
 always @(posedge clk) 
 begin
  if(sync_reset==1'b1)
   Q <= 1'b0; 
  else 
   Q <= D; 
 end 
endmodule 


