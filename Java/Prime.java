class Primes {
    boolean isprime(long x) {
        String[] list_taboo_digits = {"0", "2", "4", "5", "6", "8"};
        if (x < 2 || Array.asList(list_taboo_digits).contains(String.valueOf(x).charAt(0))) {
            return false;
        }
        for (long y = 2; y <= (long) Math.sqrt(x); y++) {
            if (x % y == 0) {
                return false;
            }
        }
        return true;
    }

    void primes(long start, long finish) {
        for (long i = start; i < finish; i++) {
            if (isprime((long) i)) {
                System.out.println((long) i);
            }
        }
    }

    public static void main(String[] args) {
        Primes primes = new Primes();
        System.out.println(primes.isprime(1));
        primes.primes(1, 100);
    }
}
