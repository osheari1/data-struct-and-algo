#[macro_use] extern crate itertools;
pub mod money_change;
pub mod max_value_of_loot;
pub mod max_number_of_prizes;

//use money_change;
//use max_value_of_loot;
fn main() {
    max_number_of_prizes::main::main();
//    max_value_of_loot::main::main();
//    max_value_of_loot::stress_test::run_stress_test();
}
