use std::{fs, arch::x86_64::_SIDD_BIT_MASK};

use regex::Regex;

fn get_nums(_string: &str) -> String{
    let re = Regex::new(r"\D").unwrap();    
    let output =re.replace_all(_string,"").to_string();
    
    return output;
}

fn find_digit_name(_string: String) -> String{
    let mut _string = _string.replace("one", "one1one");
    let mut _string = _string.replace("two", "two2two");
    let mut _string = _string.replace("three", "three3three");
    let mut _string = _string.replace("four", "four4four");
    let mut _string = _string.replace("five", "five5five");
    let mut _string = _string.replace("six", "six6six");
    let mut _string = _string.replace("seven", "seven7seven");
    let mut _string = _string.replace("eight", "eight8eight");
    let mut _string = _string.replace("nine", "nine9nine");
    return _string;
}

fn get_line_value(_string: &str) -> i32{
    
    let hold = get_nums(_string);
    //println!("{}",hold);
    if hold.len() == 1{

        return (hold.chars().nth(0).unwrap().to_string() + hold.chars().nth(0).unwrap().to_string().as_str()).parse::<i32>().unwrap();
        
    }
    else if hold.len() == 2 {
        return (hold).parse::<i32>().unwrap();
    }
    else{
        return (hold.chars().nth(0).unwrap().to_string() + hold.chars().nth(hold.len()-1).unwrap().to_string().as_str()).parse::<i32>().unwrap();
    }
    
    
}

fn main() {
    let mut total: i32 = 0;
    let file = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in file.lines() {
        //println!("{}",line);
        total += get_line_value(&find_digit_name(line.to_string()));
    }
    
    println!("{}",total);
}

