use std::collections::HashSet;

use glam::IVec3;
use itertools::Itertools;

fn main() -> anyhow::Result<()> {
    let file = include_str!("input.txt");
    let mut cubes = HashSet::new();
    for line in file.lines() {
        let tokens: Vec<i32> = line.split(',').map(str::parse).try_collect()?;
        cubes.insert(IVec3::from_slice(&tokens));
    }
    let total_area = 6 * cubes.len();
    let overlap = 2 * cubes
        .iter()
        .tuple_combinations()
        .filter(|(&a, &b)| (a - b).dot(a - b) == 1)
        .count();
    println!("part 1: {}", total_area - overlap);
    println!("part 2: {}", visible_area(&cubes));
    Ok(())
}

fn visible_area(cubes: &HashSet<IVec3>) -> u32 {
    let max = cubes
        .iter()
        .copied()
        .fold(IVec3::splat(i32::MIN), IVec3::max)
        + IVec3::ONE;
    let min = cubes
        .iter()
        .copied()
        .fold(IVec3::splat(i32::MAX), IVec3::min)
        - IVec3::ONE;
    let steps = [
        IVec3::X,
        IVec3::Y,
        IVec3::Z,
        IVec3::NEG_X,
        IVec3::NEG_Y,
        IVec3::NEG_Z,
    ];
    let mut queue = vec![IVec3::ZERO];
    let mut visited = HashSet::new();
    let mut area = 0;
    while let Some(coords) = queue.pop() {
        if visited.contains(&coords) || coords.cmplt(min).any() || coords.cmpgt(max).any() {
            continue;
        }
        for step in steps {
            let next = coords + step;
            if cubes.contains(&next) {
                area += 1;
            } else {
                queue.push(next);
            }
        }
        visited.insert(coords);
    }
    area
}
