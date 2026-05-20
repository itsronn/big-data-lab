x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 5, 4, 5)

cat("Covariance: ", cov(x, y), "\n")
cat("Correlation:", cor(x, y), "\n")

# Correlation matrix
data <- data.frame(x, y)
cat("Correlation Matrix:\n")
print(cor(data))


x <- c(2, 4, 6, 8, 10)
y <- c(1, 3, 5, 7, 9)

n <- length(x)

# Means
x_mean <- sum(x) / n
y_mean <- sum(y) / n

# Covariance
cov_result <- sum((x - x_mean) * (y - y_mean)) / (n - 1)
cat("Covariance:", cov_result, "\n")

# Standard deviations
sd_x <- sqrt(sum((x - x_mean)^2) / (n - 1))
sd_y <- sqrt(sum((y - y_mean)^2) / (n - 1))

# Correlation
cor_result <- cov_result / (sd_x * sd_y)
cat("Correlation:", cor_result, "\n")