class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int x = 0;
        int y = 0;
        char dir = 'N';
        int maxDistSqr = 0;

        Set<Pair<Integer, Integer>> obstacleLocations = new HashSet<>();
        for (int[] ob : obstacles) {
            obstacleLocations.add(new Pair(ob[0], ob[1]));
        }

        for (int i = 0; i < commands.length; i++) {
            int curr = commands[i];
            if (curr == -2) {
                dir = turnLeft(dir);
            } else if (curr == -1) {
                dir = turnRight(dir);
            } else {
                for (int j = 0; j < curr; j++) {
                    if (dir == 'N') {
                        if (!obstacleLocations.contains(new Pair(x, y + 1))) {
                            y++;
                        } else {
                            break;
                        }
                    } else if (dir == 'S') {
                        if (!obstacleLocations.contains(new Pair(x, y - 1))) {
                            y--;
                        } else {
                            break;
                        }
                    } else if (dir == 'W') {
                        if (!obstacleLocations.contains(new Pair(x - 1, y))) {
                            x--;
                        } else {
                            break;
                        }
                    } else {
                        // 'E'
                        if (!obstacleLocations.contains(new Pair(x + 1, y))) {
                            x++;
                        } else {
                            break;
                        }
                    }
                }
            }
            maxDistSqr = Math.max(maxDistSqr, x * x + y * y);
        }
        return maxDistSqr;
    }

    private char turnLeft(char currDir) {
        if (currDir == 'N') {
            return 'W';
        } else if (currDir == 'W') {
            return 'S';
        } else if (currDir == 'S') {
            return 'E';
        } else {
            // currDir = 'E'
            return 'N';
        }
    }

    private char turnRight(char currDir) {
        if (currDir == 'N') {
            return 'E';
        } else if (currDir == 'E') {
            return 'S';
        } else if (currDir == 'S') {
            return 'W';
        } else {
            return 'N';
        }
    }
}
