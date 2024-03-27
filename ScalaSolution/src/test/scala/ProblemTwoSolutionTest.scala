import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import problemTwo._

class ProblemTwoSolutionTest extends AnyFlatSpec with Matchers {

  val promotions: Seq[Promotion] = Seq(
      Promotion("P1", Seq("P3")),
      Promotion("P2", Seq("P4", "P5")),
      Promotion("P3", Seq("P1")),
      Promotion("P4", Seq("P2")),
      Promotion("P5", Seq("P2")),
  )

  it should "return all combinable promotions" in {
    val allCombos = ProblemTwoSolution.allCombinablePromotions(promotions)
    val expectedCombos = Seq(
      PromotionCombo(Seq("P1", "P2")),
      PromotionCombo(Seq("P2", "P3")),
      PromotionCombo(Seq("P1", "P4", "P5")),
      PromotionCombo(Seq("P3", "P4", "P5"))
    )
    allCombos should contain theSameElementsAs expectedCombos
  }


  it should "return combinable promotions for a specific promotion code" in {
    val promotionCode1 = "P1"
    val combinable1 = ProblemTwoSolution.combinablePromotions(promotionCode1, promotions)
    val expectedCombinable1 = Seq(
      PromotionCombo(Seq("P1", "P2")),
      PromotionCombo(Seq("P1", "P4", "P5"))
    )
    combinable1 should contain theSameElementsAs expectedCombinable1

    val promotionCode2 = "P3"
    val combinable2 = ProblemTwoSolution.combinablePromotions(promotionCode2, promotions)
    val expectedCombinable2 = Seq(
      PromotionCombo(Seq("P2", "P3")),
      PromotionCombo(Seq("P3", "P4", "P5"))
    )
    combinable2 should contain theSameElementsAs expectedCombinable2

    val promotionCode3 = "P6" // No combinable promotions for this code
    val combinable3 = ProblemTwoSolution.combinablePromotions(promotionCode3, promotions)
    combinable3 shouldBe empty
  }
}
