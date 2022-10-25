// this is pine script
study(title = "Fibonacci EMAMA", overlay = true)

SMA1 = input(8)
sma8 = sma(close, SMA1)
plot(sma8, linewidth = 1, color = color.red, title = "SMA1")

SMA2 = input(21)
sma21 = sma(close, SMA2)
plot(sma21, linewidth = 1, color = color.orange, title = "SMA2")

SMA3 = input(55)
sma55 = sma(close, SMA3)
plot(sma55, linewidth = 2, color = color.yellow, title = "SMA3")

SMA4 = input(100)
sma100 = sma(close, SMA4)
plot(sma100, linewidth = 4, color = color.green, title = "SMA4")

SMA5 = input(200)
sma200 = sma(close, SMA5)
plot(sma200, linewidth = 4, color = color.blue, title = "SMA5")

// emas now

EMA1 = input(8)
ema8 = ema(close, SMA1)
plot(ema8, linewidth = 1, color = color.red, title = "EMA1")

EMA2 = input(21)
ema21 = ema(close, EMA2)
plot(ema21, linewidth = 1, color = color.orange, title = "EMA2")

EMA3 = input(55)
ema55 = ema(close, EMA3)
plot(ema55, linewidth = 2, color = color.yellow, title = "EMA3")

EMA4 = input(100)
ema100 = ema(close, EMA4)
plot(ema100, linewidth = 3, color = color.green, title = "EMA4")

EMA5 = input(200)
ema200 = ema(close, EMA5)
plot(ema200, linewidth = 4, color = color.blue, title = "EMA5")
