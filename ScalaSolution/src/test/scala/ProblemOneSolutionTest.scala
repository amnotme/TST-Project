import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import problemOne.{CabinPrice, Rate, BestGroupPrice}
import problemOne.ProblemOneSolution._

class ProblemOneSolutionTest extends AnyFlatSpec with Matchers {

  it should "return the best group prices for given rates and prices" in {
    val rates = Seq(Rate("M1", "Military"), Rate("S1", "Senior"))
    val prices = Seq(
      CabinPrice("C1", "M1", 100),
      CabinPrice("C1", "S1", 150),
      CabinPrice("C2", "M1", 200),
      CabinPrice("C2", "S1", 250)
    )

    val expected = Seq(
      BestGroupPrice("C1", "M1", 100, "Military"),
      BestGroupPrice("C2", "M1", 200, "Military"),
      BestGroupPrice("C1", "S1", 150, "Senior"),
      BestGroupPrice("C2", "S1", 250, "Senior")
    )

    val result = getBestGroupPrices(rates, prices)
    result should contain theSameElementsAs expected
  }


  it should "return an empty sequence if rates or prices are empty" in {
    val result1 = getBestGroupPrices(Seq.empty, Seq.empty)
    result1 shouldBe empty

    // Ensure that the rates sequence contains a rate with the code "M1"
    val ratesWithM1 = Seq(Rate("M1", "Military"))

    val result2 = getBestGroupPrices(ratesWithM1, Seq.empty)
    result2 shouldBe empty

    val result3 = getBestGroupPrices(Seq.empty, Seq(CabinPrice("C1", "M1", 100)))
    result3 shouldBe empty
  }

}
