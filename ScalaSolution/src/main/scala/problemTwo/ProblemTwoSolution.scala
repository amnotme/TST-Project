package problemTwo

import scala.collection.mutable.ArrayBuffer
import problemTwo.ProblemTwoSolution.{allCombinablePromotions, combinablePromotions}
import Data.getInputPromotions

object ProblemTwoSolution {
  def allCombinablePromotions(allPromotions: Seq[Promotion]): Seq[PromotionCombo] =
    // 1. Iterates through all possible combinations of all the promotions
    // 2. Identifies if the combination is valid
    // 3. Filters possible maximal combinations(that is, all combinations without repeating of longest possible length)
    // 4. Converts maximal combinations back to a list creates instances of PromotionCombo
    val maximalCombos = ArrayBuffer.empty[Set[String]]
    val potentialCombos = ArrayBuffer.empty[Set[String]]

    for (idx <- 1 to allPromotions.length)
      for (combination <- allPromotions.combinations(idx))
        val combinationSet = combination.map(_.code).toSet
        if (isCombinationValid(combination))
          potentialCombos += combinationSet

    getMaximalCombination(
      potentialCombos,
      maximalCombos
    )

    // Convert maximal combinations to PromotionCombo objects
    maximalCombos.map(combo => PromotionCombo(combo.toSeq.sorted)).toSeq

  private def getMaximalCombination(potentialCombos: ArrayBuffer[Set[String]], maximalCombos: ArrayBuffer[Set[String]]): Unit =
    // Filter out non-maximal combinations from the potential combinations.
    for (combo <- potentialCombos)
      var isMaximal = true
      for (otherCombo <- potentialCombos if otherCombo != combo)
        if (combo.subsetOf(otherCombo))
          isMaximal = false
      if (isMaximal)
        maximalCombos += combo

  private def isCombinationValid(combos: Seq[Promotion]): Boolean =
    // Check if a given combination of promotions is valid(i.e., all promotions can be combined).
    // 1. It iterates through a tuple of possible combinations and checks that:
    // 2  PromoCode from isn 't in any other notCombinableWith Seq from evey other Promotion
    for {
      i <- combos.indices
      promo = combos(i)
      // Avoid comparing a promotion with itself and ensure each pair is checked only once.
      promoTwo <- combos.drop(i + 1) if promoTwo.notCombinableWith.contains(promo.code) || promo.notCombinableWith.contains(promoTwo.code)
    } return false
    true


  def combinablePromotions(promotionCode: String, allPromotions: Seq[Promotion]): Seq[PromotionCombo] =
    //  Given a Seq of Promotions, it returns a list of filtered PromotionCombos that match the promotionCode
    allCombinablePromotions(allPromotions)
      .filter(promotion => promotion.promotionCodes
        .contains(promotionCode)
      )

}


object RunProblemTwo {
  def problemTwoRun: Unit =
    val allCombinations = allCombinablePromotions(
      allPromotions = getInputPromotions
    )

    val combinable_solution_one = combinablePromotions(
      promotionCode = "P1",
      allPromotions = getInputPromotions
    )

    val combinable_solution_two = combinablePromotions(
      promotionCode = "P3",
      allPromotions = getInputPromotions
    )

    for (result <- Seq(allCombinations, combinable_solution_one, combinable_solution_two)) {
      result.foreach(println)
    }
}