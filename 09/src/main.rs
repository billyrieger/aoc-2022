use std::collections::HashSet;

use anyhow::anyhow;
use glam::IVec2;

fn main() -> anyhow::Result<()> {
    let file = std::fs::read_to_string(std::env::args().nth(1).ok_or(anyhow!("no input file"))?)?;
    let mut inputs: Vec<(IVec2, i32)> = vec![];
    for line in file.lines() {
        let (dir, num) = line.split_once(' ').ok_or(anyhow!("malformed input"))?;
        let num: i32 = num.parse()?;
        let dir = match dir {
            "R" => IVec2::X,
            "L" => IVec2::NEG_X,
            "U" => IVec2::Y,
            "D" => IVec2::NEG_Y,
            _ => panic!("bad direction"),
        };
        inputs.push((dir, num));
    }
    println!("part 1: {}", simulate(&inputs, 2));
    println!("part 2: {}", simulate(&inputs, 10));
    Ok(())
}

fn simulate(inputs: &[(IVec2, i32)], rope_len: usize) -> usize {
    let mut rope = vec![IVec2::ZERO; rope_len];
    let mut visited: HashSet<IVec2> = HashSet::from_iter([IVec2::ZERO]);
    for &(dir, num) in inputs {
        for _ in 0..num {
            rope[0] += dir;
            update(&mut rope);
            visited.insert(*rope.last().unwrap());
        }
    }
    visited.len()
}

fn update(rope: &mut [IVec2]) {
    for i in 0..(rope.len() - 1) {
        let (head, tail) = (rope[i], &mut rope[i + 1]);
        let delta = head - *tail;
        if delta.x.abs() > 1 || delta.y.abs() > 1 {
            *tail += IVec2::new(delta.x.signum(), delta.y.signum());
        }
    }
}
