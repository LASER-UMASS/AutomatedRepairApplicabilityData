/*
* This file is used for computing relevant test methods for Defects4J defects  
* This file is borrowed from https://bitbucket.org/rjust/fault-localization-data/src/5efecb4dcc7aa9cd60f01745ecdffe784f6fff9e/killmap/?at=master
*/


public class TestMethod implements Comparable<TestMethod> {

  private final Class<?> testClass;

  private final String name;

  private static final char SEPARATOR = '#';

  public TestMethod(Class<?> testClass, String name) {
    this.testClass = testClass;
    this.name = name;
  }

  public Class<?> getTestClass() {
    return this.testClass;
  }

  public String getName() {
    return this.name;
  }

  @Override
  public int hashCode() {
    return 37 * 19 * this.toString().hashCode();
  }

  @Override
  public boolean equals(Object obj) {
    if (obj instanceof TestMethod) {
      TestMethod other = (TestMethod) obj;
      return this.toString().equals(other.toString());
    }
    return false;
  }

  public int compareTo(TestMethod obj) {
    if (obj instanceof TestMethod) {
      TestMethod other = (TestMethod) obj;
      return this.toString().compareTo(other.toString());
    }
    return -1;
  }

  @Override
  public String toString() {
    return this.testClass.getName() + SEPARATOR + this.name;
  }
}
