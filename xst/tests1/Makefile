all: adder_8 mult4_bb adder adder16 full_adder te top SRS rx re pwm pwmN adder2_bb adder4_bb addS accumS

D_ADDER2_BB = ./tb_adder2_bb.v ../accumulators.v
N_ADDER2_BB = adder2_bb

D_ADDER4_BB = ./tb_adder4_bb.v ../accumulators.v
N_ADDER4_BB = adder4_bb

D_MULT4_BB = tb_mult4_bb.v ../multipliers.v ../accumulators.v
N_MULT4_BB = mult4_bb



adder_8: tb_adder_8.v ../accumulators.v
	iverilog -o adder_8.sim tb_adder_8.v ../accumulators.v 
	./adder_8.sim
	
adder: tb_adder.v ../accumulators.v
	iverilog -o adder.sim tb_adder.v ../accumulators.v
	./adder.sim

adder16: tb_adder16.v ../accumulators.v
	iverilog -o adder16.sim tb_adder16.v ../accumulators.v
	./adder16.sim

full_adder: tb_full_adder.v ../accumulators.v
	iverilog -o full_adder.sim tb_full_adder.v ../accumulators.v
	./full_adder.sim

te: tb_te.v ../shift_registers.v
	iverilog -o te.sim tb_te.v ../shift_registers.v
	./te.sim

top: tb_top.v ../counters.v
	iverilog -o top.sim tb_top.v ../counters.v
	./top.sim

SRS: tb_SRS.v ../shift_registers.v
	iverilog -o SRS.sim tb_SRS.v ../shift_registers.v
	./SRS.sim

rx: tb_rx.v ../counters.v ../three_st.v
	iverilog -o rx.sim tb_rx.v ../counters.v ../three_st.v
	./rx.sim

re: tb_re.v ../counters.v ../uart.v
	iverilog -o re.sim tb_re.v  ../counters.v ../uart.v
	./re.sim


pwm: tb_pwm.v ../one_shot.v
	iverilog -o pwm.sim tb_pwm.v ../one_shot.v
	./pwm.sim

pwmN: tb_pwmN.v ../one_shot.v
	iverilog -o pwmN.sim tb_pwmN.v ../one_shot.v
	./pwmN.sim

$(N_ADDER2_BB): $(D_ADDER2_BB)
	iverilog -o $(N_ADDER2_BB).sim $(D_ADDER2_BB)
	./$(N_ADDER2_BB).sim

$(N_ADDER4_BB): $(D_ADDER4_BB)
	iverilog -o $(N_ADDER4_BB).sim $(D_ADDER4_BB)
	./$(N_ADDER4_BB).sim

$(N_MULT4_BB): $(D_MULT4_BB)
	iverilog -o $(N_MULT4_BB).sim $(D_MULT4_BB)
	./$(N_MULT4_BB).sim



clean:
	rm *.sim *.vcd
