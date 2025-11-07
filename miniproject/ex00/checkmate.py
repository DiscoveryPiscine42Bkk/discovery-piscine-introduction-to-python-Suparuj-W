def checkmate(board):
    try:
        lines = [line for line in board.splitlines() if line.strip() != ""]
        if not lines:
            print("Fail")
            return

        grid = [list(line) for line in lines]
        rows = len(grid)
        cols = rows
        for i in range(rows):
            if (cols != len(grid[i])):
                print("Error")
                return

        king = None
        for i in range(rows):
            for j in range(len(grid[i])):
                if grid[i][j] == "K":
                    king = (i, j)
                    break
            if king:
                break

        if not king:
            print("Fail")
            return

        kx, ky = king

        def in_bounds(x, y):
            return 0 <= x < rows and 0 <= y < len(grid[x])

        for dx, dy in [(1, -1), (1, 1)]:
            nx, ny = kx + dx, ky + dy
            if in_bounds(nx, ny) and grid[nx][ny] == "P":
                print("Success")
                return

        straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in straight_dirs:
            nx, ny = kx + dx, ky + dy
            while in_bounds(nx, ny):
                ch = grid[nx][ny]
                if ch != '.':
                    if ch == 'R' or ch == 'Q':
                        print("Success")
                        return
                    else:
                        break
                nx += dx
                ny += dy

        diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in diag_dirs:
            nx, ny = kx + dx, ky + dy
            while in_bounds(nx, ny):
                ch = grid[nx][ny]
                if ch != '.':
                    if ch == 'B' or ch == 'Q':
                        print("Success")
                        return
                    else:
                        break
                nx += dx
                ny += dy

        print("Fail")

    except Exception:
        print("Fail")