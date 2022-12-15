#![feature(array_windows)]

use anyhow::anyhow;
use anyhow::Result;
use std::collections::HashSet;

const START_COORDS: Coords = Coords::new(500, 0);

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Coords {
    x: i32,
    y: i32,
}

impl Coords {
    const fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    fn offset(&self, dx: i32, dy: i32) -> Self {
        Self::new(self.x + dx, self.y + dy)
    }

    fn parse(s: &str) -> Result<Self> {
        let (x, y) = s
            .trim()
            .split_once(',')
            .ok_or_else(|| anyhow!("split string error"))?;
        Ok(Self::new(x.parse()?, y.parse()?))
    }
}

fn min_max(x: i32, y: i32) -> (i32, i32) {
    (x.min(y), x.max(y))
}

#[derive(Clone, Debug)]
struct Universe {
    occupied: HashSet<Coords>,
    max_height: i32,
}

impl Universe {
    fn new() -> Self {
        Self {
            occupied: HashSet::new(),
            max_height: i32::MIN,
        }
    }

    fn draw_line(&mut self, start: Coords, end: Coords) {
        if start.x == end.x {
            let (y_min, y_max) = min_max(start.y, end.y);
            self.max_height = self.max_height.max(y_max);
            for y in y_min..(y_max + 1) {
                self.occupied.insert(Coords::new(start.x, y));
            }
        } else if start.y == end.y {
            self.max_height = self.max_height.max(start.y);
            let (x_min, x_max) = min_max(start.x, end.x);
            for x in x_min..(x_max + 1) {
                self.occupied.insert(Coords::new(x, start.y));
            }
        } else {
            panic!("line does not lie on grid");
        }
    }

    fn rest_coords(&self, start: Coords, floor: bool) -> Option<Coords> {
        if self.occupied.contains(&start) {
            return None;
        }
        let mut current = start;
        loop {
            if current.y == self.max_height + 1 {
                return if floor { Some(current) } else { None };
            }

            let down = current.offset(0, 1);
            let down_left = current.offset(-1, 1);
            let down_right = current.offset(1, 1);

            if !self.occupied.contains(&down) {
                current = down;
            } else if !self.occupied.contains(&down_left) {
                current = down_left;
            } else if !self.occupied.contains(&down_right) {
                current = down_right;
            } else {
                return Some(current);
            }
        }
    }

    fn drop_sand(&mut self, floor: bool) -> u32 {
        let mut counter = 0;
        while let Some(rest_coords) = self.rest_coords(START_COORDS, floor) {
            self.occupied.insert(rest_coords);
            counter += 1;
        }
        counter
    }
}

fn main() -> Result<()> {
    let mut universe = Universe::new();
    let input = std::fs::read_to_string("input.txt")?;

    for line in input.lines() {
        let coords: Vec<Coords> = line
            .split(" -> ")
            .map(Coords::parse)
            .collect::<Result<_>>()?;
        for &[start, end] in coords.array_windows() {
            universe.draw_line(start, end);
        }
    }

    let part_1 = universe.clone().drop_sand(false);
    println!("part 1: {part_1}");

    let part_2 = universe.drop_sand(true);
    println!("part 2: {part_2}");

    Ok(())
}
