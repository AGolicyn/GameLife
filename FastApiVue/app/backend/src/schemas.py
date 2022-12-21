from pydantic import BaseModel, validator, Field


class Molecule(BaseModel):
    row: int
    col: int

    @validator('*')
    def row_must_be_zero_positive(cls, val):
        if val < 0:
            raise ValueError('Coords must be zero or greater')
        return val


class AliveMolecules(BaseModel):
    molecules: list[str | Molecule] = Field(alias='alive_mols')

    @validator('molecules')
    def must_contain_separator_and_integers(cls, mols):
        result = []
        for mol in mols:
            if '-' not in mol:
                raise ValueError('Coords must be separated by "-"')
            nums = mol.split('-')
            try:
                result.append(tuple(int(num) for num in nums))
            except ValueError:
                raise ValueError('Coords must be integers')
        return result

    @validator('molecules')
    def must_be_convertable_to_molecule_instance(cls, mols: tuple[int, int]):
        try:
            result = [Molecule(row=row, col=col) for row, col in mols]
        except ValueError:
            raise ValueError
        return result


class PlayGround(BaseModel):
    row_num: int = Field(alias='width')
    col_num: int = Field(alias='len')

    @validator('*')
    def row_must_be_zero_positive(cls, val):
        if val <= 0:
            raise ValueError('Shape values must be greater then zero')
        return val


class EpochSpeed(BaseModel):
    speed: float

    @validator('speed')
    def speed_should_not_be_less_then_0(cls, val):
        if val < 0.1:
            return 0.1
        return val


class GameOptions(AliveMolecules, EpochSpeed):
    shape: PlayGround | None
    interrupt: bool
